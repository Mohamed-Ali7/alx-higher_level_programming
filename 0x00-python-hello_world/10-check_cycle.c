#include "lists.h"
/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: Is the linked list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp = list;
	listint_t *jumper = list;

	if (list == NULL)
		return (0);

	while (jumper != NULL && jumper->next != NULL)
	{
		jumper = jumper->next->next;
		tmp = tmp->next;
		if (jumper == tmp)
			return (1);
	}
	return (0);
}
