#include "lists.h"

/**
 * check_cycle - Checks if a linked list contains a cycle
 *
 * @head: A pointer to the head of the linked list
 *
 * Return: 1 if the list contains a cycle, 0 otherwise
 */
int check_cycle(listint_t *head)
{
	listint_t *slow = head, *fast = head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}

