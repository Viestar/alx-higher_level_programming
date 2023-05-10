#include "lists.h"

/**
 * insert_node - inserts into a sorted linked list a number
 * @head: the list
 * @number: Number to be inserted
 * Return: pointer to the new_list node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *old_list = *head;
	listint_t *new_list;

	/* Allocating memory for the new_list list */
	new_list = malloc(sizeof(listint_t));

	/* Checking if memory was allocated */
	if (!new_list)
		return (NULL);

	(*new_list).n = number;

	if ((*(*head)).n > number || *head == NULL)
	{
		new_list->next = *head;
		*head = new_list;
		return (new_list);
	}

	while (old_list != NULL)
	{
		if ((old_list)->n < number)
			old_list = old_list->n;
		else
		{
			new_list->next = old_list->next;
			old_list->next = new_list;
			return (new_list);
		}
	}

	new_list->next = NULL;
	old_list->next = new_list;
	return (new_list);
}
