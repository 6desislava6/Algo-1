#include "Stack2.h"

Stack2::Stack2()
{

}
Stack2::~Stack2()
{
	delete queueOfElements;
}


void Stack2::push(const int & item)
{
	queueOfElements->push(item);
}

int Stack2::pop	()
{	
	// Emptying the first, filling the second.
	Queue* helperQueue = new Queue();
	int initialSize = this->queueOfElements->size();

	for (size_t i = 0; i < initialSize - 1; i++)
	{
		helperQueue->push(queueOfElements->pop());
	}
	int popped = queueOfElements->pop();
	queueOfElements = helperQueue;
	return popped;
}

int Stack2::peek()
{
	// Emptying the first, filling the second.
	Queue helperQueue;
	int initialSize = this->queueOfElements->size();

	for (size_t i = 0; i < initialSize - 1; i++)
	{
		helperQueue.push(queueOfElements->pop());
	}
	int peeked = queueOfElements->peek();
	helperQueue.push(peeked);
	*queueOfElements = helperQueue;
	return peeked;
}
unsigned Stack2::size() const
{
	return this->queueOfElements->size();
}