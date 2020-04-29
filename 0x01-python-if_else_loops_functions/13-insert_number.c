#include "lists.h"

/**
 * insert_node - inserts a node with a number in a ordered list.
 *
 * @head: dble ptr to header pointer.
 * @number: number to insert.
 *
 * Return: returns a pointer to the inserted node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node = *head;
	listint_t *aux_ptr = NULL;

	if (head == NULL)
		return (NULL);

	if (*head == NULL || current_node->n > number)
	{
		current_node = malloc(sizeof(listint_t));
		if (current_node == NULL)
			return (NULL);

		current_node->next = *head;

		current_node->n = number;
		*head = current_node;
		return (current_node);
	}

	while (current_node->next != NULL && number > (current_node->next)->n)
		current_node = current_node->next;

	if (current_node->next != NULL && (current_node->next)->n == number)
		return (NULL);
	aux_ptr = current_node;

	current_node = malloc(sizeof(listint_t));
	if (current_node == NULL)
		return (NULL);

	current_node->n = number;
	current_node->next = aux_ptr->next;
	aux_ptr->next = current_node;

	return (current_node);
}
