#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * add_nodeint - singly linked list
 * @head: structure
 * @n:value
 * Description: singly linked list node structure
 *Return: a number of elements
 * for Holberton project
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);

}

/**
 * insert_node - prints all elements of a listint_t list
 * @head: pointer to head of list
 * @number: value of node
 * Return: number of nodes
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *copy = *head;
	int auxvalue = 0, i = 0;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	while (copy->next != NULL)
	{
		auxvalue = copy->next->n;
		if (auxvalue >= number && i != 0)
		{
			new->next = copy->next;
			copy->next = new;
			return (new);
		}
		else if (auxvalue >= number && i == 0 || copy == NULL)
		{
			new->next = *head;
			*head = new;
			return (new);
		}
		copy = copy->next;
		if (copy->next == NULL)
		{
			copy->next = new;
			return (new);
		}
		i++;
	}
	return (NULL);
}
