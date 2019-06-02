#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
	struct Node * next;
};

void print_list(struct Node * head) {
    struct Node * cur = head;
	while (cur) {
	    printf("%d ", cur->data);
		cur = cur->next;
	}
	printf("\n");
}

void push_left(struct Node ** phead, int x) {
    struct Node * new = malloc(sizeof(struct Node));
	struct Node * next;
	new->data = x;
	new->next = *phead;
	*phead = new;
	next = (*phead)->next;
}

void reverse(struct Node ** phead) {
    struct Node * prev = NULL;
    struct Node * next = NULL;
    struct Node * cur = *phead;
	while (cur) {
	    next = cur->next;
		cur->next = prev;
		prev = cur;
		cur = next;
	}
	*phead = prev;
}

int main() {
    struct Node * head = NULL;
	push_left(&head, 20);
	push_left(&head, 15);
	push_left(&head, 30);
	push_left(&head, 87);
	print_list(head);
	reverse(&head);
	print_list(head);
}
