#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <dirent.h>
#include <fcntl.h>
#include <errno.h>

#define MAX_LEN_STR		256

struct my_proc {
    pid_t pid;
    char cmdline[MAX_LEN_STR];
};

struct my_proc_group {
	struct my_proc ** list;
	int len;
	//int buf_size;
};

bool true_filter(const struct my_proc * a) {
    return true;
}

char *strncpy_v2(char *dest, char *src, unsigned int size){
    if (size==0) return dest;
    dest[--size] = '\0';
    return strncpy(dest, src, size);
}

int scan_ps(struct my_proc ***ptr, bool (*filter)(const struct my_proc *)) {
    DIR * dirp;
    struct dirent * dp;
    int count = 0;
    pid_t pid;
    char path[MAX_LEN_STR], buf[MAX_LEN_STR];
    int fd, n;
    unsigned int size = 16;
    struct my_proc ** ps_list, ** ps_list2;
    struct my_proc * current_ps;

    dirp = opendir("/proc");
    if (NULL==dirp)
        return -1;

    ps_list = malloc(sizeof(*ps_list)*size);
    if (ps_list==NULL) {
        printf("%s: malloc failed(ps_list)\n",__func__);
        goto failed_closedir;
    }

    while (NULL != (dp = readdir(dirp))) {
        pid = atoi(dp->d_name);
        if (0 == pid)
            continue;
        snprintf(path, sizeof(path), "/proc/%u/cmdline", pid);
        fd = open(path, O_RDONLY);
        if (fd < 0) {
            printf("%s: failed to open() (%d)\n",__func__, errno);
            continue;
        }
        n = read(fd, buf, MAX_LEN_STR);
        if (0 == n) {
            // cmdline is empty. maybe kernel process.
            printf("%s: pid:%u cmdline is empty!\n",__func__, pid);
            close(fd);
            continue;
        }
        n = (MAX_LEN_STR - 1) > n ? n : (MAX_LEN_STR - 1);
        buf[n] = '\0';
        close(fd);

        current_ps = malloc(sizeof(*current_ps));
        if (current_ps==NULL) {
            printf("%s: malloc failed\n",__func__);
            goto failed_ps_list;
        }
        current_ps->pid = pid;
        strncpy_v2(current_ps->cmdline, buf, MAX_LEN_STR);
        if ( !filter(current_ps) ) {
            printf("%s: let it go. currnet_ps\n", __func__);
            free(current_ps);
            continue;
        }
        // prepare ps_list
        if (count!=0 && (count%16)==0) {
            size += 16;
            ps_list2 = realloc(ps_list, sizeof(*ps_list)*size);
            if (ps_list2==NULL) {
                printf("%s: malloc failed(ps_list2)\n",__func__);
                goto failed;
            }
            ps_list = ps_list2;
        }
        ps_list[count++] = current_ps;
    }
    closedir(dirp);
    *ptr = ps_list;
    return count;
failed:
    free(current_ps);
failed_ps_list:
    while(count--) {
        free(ps_list[count]);
    }
    free(ps_list);
failed_closedir:
    closedir(dirp);
    return -1;
}

int build_proc_group(struct my_proc_group * pg) {
	int n;
	n = scan_ps(&(pg->list), true_filter);
	pg->len = n;
}

int cleanup_proc_group(struct my_proc_group * pg) {
	int n = pg->len;
	while(n--) {
		free(pg->list[n]);
	}
	free(pg->list);
	return 0;
}

int init_proc_group(struct my_proc_group * pg) {
	pg->list = malloc(sizeof(*(pg->list)) * 1);
	if (NULL == pg->list) {
        printf("%s: malloc failed(ps_list)\n",__func__);
		return -1;
	}
	pg->list[0] = malloc(sizeof(*(pg->list[0])));
	if (NULL == pg->list[0]) {
        printf("%s: malloc failed(ps_list)\n",__func__);
		goto failed;
	}
	pg->len = 1;
	//pg->buf_len = 1;
	return 0;
failed:
	free(pg->list);
	return -1;
}

int add_item_proc_group(struct my_proc_group * pg, struct my_proc * item) {
	struct my_proc ** t_list;
	t_list = realloc(pg->list, sizeof(*(pg->list)) * (pg->len + 1));
	if (NULL == t_list) {
        printf("%s: malloc failed(ps_list)\n",__func__);
		return -1;
	}
	pg->list = t_list;
	pg->list[pg->len] = malloc(sizeof(*(pg->list[pg->len])));
	if (NULL == pg->list[pg->len]) {
        printf("%s: malloc failed(ps_list)\n",__func__);
		return -1;
	}
	pg->len += 1;
	//pg->buf_len = 1;
	return 0;

}

int main(){
    int n;
    //struct my_proc ** ps_list;
	struct my_proc_group g;

    n = scan_ps(&g.list, true_filter);
    if (n<0) {
        printf("%s: n=%d something wrong!\n", __func__, n);
        return -1;
    }
	g.len = n;
	//group.buf_size = n;
    printf("%s: n=%d\n", __func__, n);
    while (n--) {
        printf("%s: %u, %s\n", __func__, g.list[n]->pid, g.list[n]->cmdline);
    }
	cleanup_proc_group(&g);
    return 0;
}

