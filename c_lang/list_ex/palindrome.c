#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct node {
	struct node * next;
	struct node * prev;
	int data;
};

void init_list(struct node * head) {
	head->next = head;
	head->prev = head;
}

void list_add_gen(struct node * new, struct node * prev, struct node * next) {
	next->prev = new;
	new->next = next;
	new->prev = prev;
	prev->next = new;
}

void list_del_gen(struct node * prev, struct node * next) {
	next->prev = prev;
	prev->next = next;
}

void list_add_tail(struct node * new, struct node * head) {
	list_add_gen(new, head->prev, head);
}

void list_del_entry(struct node * e) {
	list_del_gen(e->prev, e->next);
}

struct node * reverse_list(struct node * head) {
	struct node * src = head->prev;
	struct node * res = malloc(sizeof(res));
	struct node * c;
	init_list(res);
	for (; src!=head; src = src->prev) {
		//printf("%s: (%c) src:%p src->prev:%p\n",__func__, src->data, src, src->prev);
		c = malloc(sizeof(c));
		c->data = src->data;
		list_add_tail(c, res);
	}
	return res;
}

bool compare_list(struct node * a, struct node * b) {
	struct node * x = a->next;
	struct node * y = b->next;
	for(; (x!=a); (x = x->next, y = y->next)) {
		if (y==b) return false;
		if (x->data != y->data) return false;
	}
	if (y!=b) return false;
	return true;
}

struct node * str2list(char * str) {
	struct node * head = malloc(sizeof(head));
	struct node * c;
	//printf("%s: entry %s(%c)\n",__func__,str, *str);
	init_list(head);
	for (; *str!='\0'; str++) {
		//printf("%s: (%c)\n",__func__, *str);
		//getchar();
		c = malloc(sizeof(c));
		c->data = *str;
		list_add_tail(c, head);
	}
	return head;
}

void print_list(struct node * head) {
	struct node * cur = head->next;
	for (; cur!=head; cur = cur->next) {
		printf("%d[%c:%X]\t", cur->data, cur->data, cur->data);
		printf("ptr:%p/%p/%p\t", cur->prev, cur, cur->next);
	}
}

int main(int argc, const char *argv[]) {
	char * tc[6] = {
		"hello", "wow", "break", "level", "rotator", "goodbye"
	};
	int i;
	struct node * head[6];
	struct node * rev[6];
	for (i=0; i<6; i++) {
		head[i] = str2list(tc[i]);
		//print_list(head[i]);
		rev[i] = reverse_list(head[i]);
		printf("i=%d %s\n", i, tc[i]);
		if (compare_list(rev[i],head[i]))
			printf("Palindrome\n");
		else
			printf("Not a palindrome\n");
	}

	return 0;
}

