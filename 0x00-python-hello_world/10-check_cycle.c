#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 *check_cycle - script to find a loop inside a linked list
 *Result: always return 0
 *@list: linked list
 *Return: 1 if there is a loop
 */
int check_cycle(listint_t *list)
{

	listint_t *lslow = list;
	listint_t *lfast = list;

	if (list == NULL)
		return (0);
	while (lslow && lfast && lfast->next)
	{
		lslow = lslow->next;
		lfast = lfast->next->next;
		if (lslow == lfast)
			return (1);
	}
	return (0);
}
