#include <stdexcept>
#include "Queue.h"

Queue::Queue() :elements(0), rear(nullptr), front(nullptr)
{
}

Queue::~Queue()
{
	unsigned elementsCount = this->size();
	for (unsigned i = 0; i < elementsCount; i++)
	{
		this->pop();
	}
}

void Queue::push(const int &item)
{
	Node *t = new Node;
	t->data = item;
	t->next = nullptr;
	// if our front is empty, fill it
	if (front == nullptr)
	{
		front = t;
	}
	else
	{
		rear->next = t;
	}
	rear = t;
	elements++;
}
int Queue::peek() const
{
	return front->data;
}

int Queue::pop()
{
	if (front == nullptr)
	{
		throw std::out_of_range("Nope!");
	}
	int data = front->data;
	Node* newFront = front->next;
	delete front;
	front = newFront;
	elements--;
	return data;
}
int Queue::size() const
{
	return elements;
}
//Copy construct
Queue::Queue(const Queue& q)
{	
	this->push(q.front->data);
	Node* nextNode = q.front->next;

	for (size_t i = 0; i < q.size() - 1; i++)
	{
		this->push(nextNode->data);
		nextNode = nextNode->next;
	}
}
