#include "lists.h"


/**
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t  *largest;
	listint_t *tmp;
	listint_t *prev;
	listint_t  *node;

	if (*head == NULL)
		return (NULL);

	largest = *head;
	tmp = *head;
	prev = NULL;
	node = malloc(sizeof (listint_t));

	if (node == NULL)
		return (NULL);

	node->n = number;

	if (tmp->n > number)
	{
		node->next = tmp;
		*head = node;

		return (node);
	}
	while (largest->next)
		largest = largest->next;

	if (number > largest->n)
	{
		node->next = NULL;
		largest->next = node;

		return (node);
	}
	else
	{
		while (tmp->next)
		{
			while (tmp->n < number)
			{
				prev = tmp;
				tmp = tmp->next;
			}
			prev->next = node;
			node->next = tmp;

			return (node);
		}
	}
	return (NULL);
}
