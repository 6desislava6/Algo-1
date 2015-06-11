#include <stdexcept>
#include "Stack.h"

Stack::Stack() :elements(0), top(nullptr)
{
}

Stack::~Stack(){
	unsigned el = items();
	for (unsigned i = 0; i<el; i++)
		remove();
}
unsigned Stack::items()const{
	return elements;
}
int Stack::remove(){
	if (top == nullptr)
		//It's empty
		throw std::out_of_range("It's empty!");
	Node *t = top;
	int data = t->data;
	top = t->previous;
	delete t;
	elements--;
	return data;
}
void Stack::push(const int &item){
	Node *t = new Node;
	t->data = item;
	t->previous = top;
	//Add on top
	// if our front is empty, fill it
	top = t;
	elements++;
}
int Stack::peek() const
{
	return top->data;
}
int Stack::pop()
{
	int popped = peek();
	remove();
	return popped;
}