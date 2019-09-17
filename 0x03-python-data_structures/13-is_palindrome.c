#include "lists.h"
/**
 * is_palindrome - check the code for Holberton School students.
 * @head: head of list
 * Return: Always 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *copy = *head;
	int value[1024];
	int size = 0;
	int l = 0;

	if (head == NULL || *head == NULL)
		return (1);

	while (copy != NULL)
	{
		value[size] = copy->n;
		copy = copy->next;
		size++;
	}
	size -= 1;
	while ((size - 0) > l)
	{
		if (value[l++] != value[size--])
			return (0);
	}
	return (1);
}
