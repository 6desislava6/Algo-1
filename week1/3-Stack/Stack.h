#ifndef Stack_H 
#define Stack_H 
class Stack{
public:
	Stack();
	~Stack();
	void push(const int & item);
	int remove();
	int pop();
	int peek() const;
	unsigned items() const;

private:
	struct Node{
		int data;
		Node *previous;
	};
	// Top node
	Node *top;
	unsigned elements;
};
#endif
