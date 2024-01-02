#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Is a pointer to the pointer to the first element of the list
 * @number: Is the number to insert
 * Return: The address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp;
	listint_t *new_node;

	if (head == NULL || *head == NULL)
		return (NULL);
	tmp = *head;
	new_node = malloc(sizeof(listint_t));
	new_node->n = number;
	while (tmp->next != NULL)
	{
		if (tmp->next->n > number)
			break;
		tmp = tmp->next;
	}
	new_node->next = tmp->next;
	tmp->next = new_node;
	return (*head);
}
