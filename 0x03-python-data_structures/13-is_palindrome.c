#include "lists.h"
#include <stdlib.h>

listint_t *reverse(listint_t *head);
/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Is a pointer to the pointer to the first element of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *cur = *head;
	listint_t *temp = *head;
	listint_t *jumper = *head;

	if (head == NULL || *head == NULL)
		return (1);


	while (jumper != NULL && jumper->next != NULL)
	{
		jumper = jumper->next->next;
		cur = cur->next;
	}
	cur = reverse(cur);
	while (cur != NULL)
	{
		if  (cur->n != temp->n)
			return (0);
		cur = cur->next;
		temp = temp->next;
	}
	return (1);
}
/**
 * reverse -  Reverses a listint_t linked list.
 * @head: Is a pointer to the pointer to the first node of the list
 * Return: A pointer to the first node of the reversed list
 */
listint_t *reverse(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *next = head;

	while (head != NULL)
	{
		next = head->next;
		head->next = prev;
		prev = head;
		head = next;
	}
	return (prev);
}
