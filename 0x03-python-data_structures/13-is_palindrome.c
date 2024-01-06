#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Is a pointer to the pointer to the first element of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *cur = *head;
	listint_t *jumper = *head;
	int *list = NULL;
	int size = 0;

	if (*head == NULL)
		return (1);

	while (cur != NULL)
	{
		cur = cur->next;
		size++;
	}
	if (size % 2 != 0)
		return (0);
	cur = *head;
	list = malloc(sizeof(int) * (size / 2));

	while (jumper != NULL)
	{
		list[size - 1] = cur->n;
		cur = cur->next;
		jumper = jumper->next->next;
		size--;
	}

	while (cur != NULL)
	{
		if (list[size] != cur->n)
			return (0);
		cur = cur->next;
		size++;
	}
	free(list);
	return (1);
}
