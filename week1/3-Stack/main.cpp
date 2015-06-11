#include "Queue.h"
#include "Stack.h"
#include "Stack2.h"


#include <iostream>

int main()
{
	Queue queue;
	queue.push(6);
	queue.push(1);
	queue.push(2);
	queue.push(3);
	queue.push(4);
	queue.push(5);
	queue.push(6);

	Queue q2 = queue;
	std::cout << q2.pop();
	std::cout << q2.pop();
	std::cout << q2.pop();
	std::cout << q2.pop();
	std::cout << q2.pop();
	std::cout << q2.pop();
	std::cout << q2.pop();

	Stack2 st;
	st.push(1);
	st.push(2);
	st.push(3);
	st.push(4);
	st.push(5);
	st.push(6);

	std::cout<<st.pop();
	//system("pause");
	return 0;
}
