#include "lists.h"

/**
 * insert_node - insert a number into a sorted linkedlist
 * @head: a pointer to the first node
 * @number: the giving number to be inserted
 * Return: a pointer to the inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *previous = NULL;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	while (current != NULL)
	{
		if (current->n < number)
		{
			previous = current;
			current = current->next;
		}
		else
			break;
	}
	if (previous == NULL)
	{
		new->next = current;
		*head = new;
	}
	else
	{
		previous->next = new;
		new->next = current;
	}
	return (new);
}
