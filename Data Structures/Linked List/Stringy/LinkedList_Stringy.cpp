// using non-pointer object

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
        cout << currentNode.value << " -> ";
        currentNode = *currentNode.nextNode;

        if (currentNode.nextNode == NULL)
        {
            cout << currentNode.value << endl;
            break;
        }
    }
}

//! insertion start
// Add a node in the front
void addInFront(StringyNode &newNode, StringyNode &head)
{
    newNode.nextNode = &head;
}

// Add a node in the middle after a specified node or end
void addInMiddle(StringyNode &newNode, StringyNode &prevNode)
{
    newNode.nextNode = prevNode.nextNode;
    prevNode.nextNode = &newNode;
}
//! insertion end

//! deletion start
// Delete first node
void deleteFront(StringyNode &head)
{
    StringyNode newHead = *head.nextNode;

    // delete &head; -> it does not deallocate the memory as head is not a pointer object

    printStringyLinkList(newHead);
}

void deleteMiddle(StringyNode &nodeDelete, StringyNode &head)
{
    StringyNode *prev = &head;
    while (true)
    {
        if (prev->nextNode == &nodeDelete)
        {
            break;
        }
        prev = prev->nextNode;
    }

    prev->nextNode = nodeDelete.nextNode;

    printStringyLinkList(head);
}

//! deletion end

int main()
{
    StringyNode node1(5);
    StringyNode node2(7);
    StringyNode node3(9);
    StringyNode node4(11);

    node1.nextNode = &node2;
    node2.nextNode = &node3;
    node3.nextNode = &node4;

    printStringyLinkList(node1);

    // //! insertion
    // {
    //     // adding a node in front
    //     printf("Inserting beginning\n");
    //     StringyNode node5(100);
    //     addInFront(node5, node1);
    //     printStringyLinkList(node5);

    //     // // adding a node in middle
    //     // printf("\nInserting middle\n");
    //     // StringyNode node6(150);
    //     // addInMiddle(node6, node2);
    //     // printStringyLinkList(node1);

    //     // // adding a node in end
    //     // printf("\nInserting ending\n");
    //     // StringyNode node7(250);
    //     // addInMiddle(node7, node4);
    //     // printStringyLinkList(node1);
    // // }

    // //! deletion
    // {
    //     printf("Deleting beginning\n");
    //     deleteFront(node1);

    //     // printf("Deleting middle\n");
    //     // deleteMiddle(node3, node1);

    //     // printf("Deleting middle\n");
    //     // deleteMiddle(node4, node1);
    // }

    return 0;
}