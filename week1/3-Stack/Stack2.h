#include "Queue.h"
#ifndef Stack2_H 
#define Stack2_H 
class Stack2{
public:
	Stack2();
	~Stack2();
	void push(const int & item);
	int pop();
	int peek();
	unsigned size() const;

private:
	// Implemented by using custom Queue
	Queue* queueOfElements = new Queue();
};
#endif
