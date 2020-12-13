#include "lists.h"

/**
 *check_cycle - checks for a cycle in a linked list
 *@list: head of the linked list
 *return - 1 if cycle present, 0 if cycle absent
 */

int check_cycle(listint_t *list)
{
	if (list == NULL)
		return (0);

	listint_t *first;
	listint_t *other;

	other = first = list;

	while (1)
	{
		first = first->next;

		if (other->next != NULL)
			other = other->next->next;

		else
			return (0);
		if (first == NULL || other == NULL)
			return (0);

		if (first == other)
			return (1);
	}
}
