#ifndef QUEUE_H 
#define QUEUE_H 
class Queue{
private:
	struct Node{
		int data;
		Node *next;
	};
	// Back of queue
	Node *rear;
	//Beginning of a queue
	Node *front;
	//number of elements
	unsigned elements;
public:
	//Constructors
	Queue();
	Queue(const Queue&);

	//Destructors
	~Queue();
	//Trivia
	void push(const int & item);
	int peek() const;
	int pop();
	int size() const;
};
#endif
