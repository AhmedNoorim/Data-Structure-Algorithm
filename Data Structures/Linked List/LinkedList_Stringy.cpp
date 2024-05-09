#include <iostream>
using namespace std;

//! structure of the LinkList_Stringy
struct StringyNode
{
    int value;
    StringyNode *nextNode;

    StringyNode() : value(-1), nextNode(NULL){};
    StringyNode(int value) : value(value), nextNode(NULL){};
};

// Printing the linkList
void printStringyLinkList(StringyNode &head)
{
    StringyNode currentNode = head;
    while (true)
    {
        cout << currentNode.value << endl;
        currentNode = *currentNode.nextNode;

        if (currentNode.nextNode == NULL)
        {
            cout << currentNode.value << endl;
            break;
        }
    }
}

// Add a node in the front
void addInFront(StringyNode &newNode, StringyNode &head)
{
    newNode.nextNode = &head;
}

// Add a node in the middle after a specified node
void addInMiddle(StringyNode &newNode, StringyNode &prevNode)
{
    newNode.nextNode = prevNode.nextNode;
    prevNode.nextNode = &newNode;
}

// Add a node in the end
void addInEnd(StringyNode &newNode, StringyNode &tail)
{
    tail.nextNode = &newNode;
    newNode.nextNode = NULL;
}

int main()
{
    StringyNode node1(5);
    StringyNode node2(7);
    StringyNode node3(9);
    StringyNode node4(11);

    node1.nextNode = &node2;
    node2.nextNode = &node3;
    node3.nextNode = &node4;

    // printStringyLinkList(node1);

    //! insertion
    {
        // adding a node in front
        printf("Inserting beginning\n");
        StringyNode node5(100);
        addInFront(node5, node1);
        printStringyLinkList(node5);

        // adding a node in middle
        printf("\nInserting middle\n");
        StringyNode node6(150);
        addInMiddle(node6, node2);
        printStringyLinkList(node1);

        // adding a node in end
        printf("\nInserting ending\n");
        StringyNode node7(250);
        addInEnd(node7, node4);
        printStringyLinkList(node1);
    }

    return 0;
}