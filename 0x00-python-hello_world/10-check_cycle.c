#include "lists.h"

/**
 * check_cycle -  Checks if a singly linked lists has a cycle in it.
 * @list: linked list to be chaecked.
 * Return: 1 if there is a cycle or 0 if not.
 */

int check_cycle(listint_t *list)
{
	listint_t *chopper, *airjet;

	/* Checking it a list is not empty */
	if (!list)
		return (0);

	/* Creating the two list clones to use for cycle checking */
	chopper = list;
	airjet = (*list).next;

	while (airjet && (*airjet).next)
	{
		/* Checking if the two planes ever meet again */
		if (airjet != chopper)
		{
			chopper = (*chopper).next;
			airjet = (*airjet).next->next;
		}
		return (1);
	}
	return (0);
}
