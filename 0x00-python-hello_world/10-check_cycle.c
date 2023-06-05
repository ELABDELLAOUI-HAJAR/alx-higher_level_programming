#include "lists.h"

/**
 * check_cycle - checks the existing of a cycle in linked list
 * @list : pointer to tha head of the linked list
 * Return: 0 - if there is no cycle in the linked list
 * 1 - if there is a cycle in the linked list
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list->next;
	fast = list->next->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
