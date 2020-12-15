#include "lists.h"


/**
 */

listint_t *insert_node(listint_t **head, int number)
{
	if (*head == NULL)
		return (NULL);

	listint_t  *largest = *head;
	listint_t *tmp = *head;
	listint_t *prev = NULL;
	listint_t  *node = malloc(sizeof (listint_t));

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
