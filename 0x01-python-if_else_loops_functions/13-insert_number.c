#include<stdio.h>
#include<stdlib.h>
#include <string.h>
#include "lists.h"

/**
 * insert_node - insert node in a linked list
 *
 * @head: pointer to the first node of the linked list
 *
 * @number: integer value of the new node to insert
 *
 * Return: the head of the linked list with the new node inserted
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_head = malloc(sizeof(listint_t));
	listint_t *tmp = *head;

	if (new_head == NULL)
	{
		return (NULL);
	}
	if (tmp == NULL)
	{
		new_head->n = number;
		new_head->next = NULL;
		(*head) = new_head;
		return (new_head);
	}
	if (tmp->next == NULL || number == 0)
	{
		if (number < tmp->n)
		{
			new_head->n = number;
			new_head->next = tmp;
			(*head) = new_head;
			return (new_head);
		}
	}
	while (tmp->next)
	{
		if ((number >= tmp->n) && (number <= tmp->next->n))
		{
			new_head->n = number;
			new_head->next = tmp->next;
			tmp->next = new_head;
			return (new_head);
		}
		tmp = tmp->next;
	}
	new_head->n = number;
	new_head->next = NULL;
	tmp->next = new_head;
	return (new_head);
}
