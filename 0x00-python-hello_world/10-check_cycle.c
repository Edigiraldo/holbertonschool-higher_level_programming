#include "lists.h"

/**
 * check_cycle - look if the linked list has a loop.
 *
 * @list: - header to linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *current_node = list;

	while (current_node != NULL)
	{
		list = head;
		while (list != current_node)
		{
			if (list == current_node->next)
				return (1);
			list = list->next;
		}
		current_node = current_node->next;
	}
	return (0);
}
