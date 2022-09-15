#include <iostream>
#include <algorithm>
#include <vector>
#define MAX_NODE 1000000 + 1
using namespace std;
typedef struct node
{
    unsigned int data;
    node *left_child;
    node *right_child;
} node;


void postorder(node *n)
{
    if (n->left_child)
        postorder(n->left_child);
    if (n->right_child)
        postorder(n->right_child);
    printf("%u\n", n->data);
}


node* make_node(unsigned int key){
    node* res = new node;
    res->data = key;
    res ->left_child = res->right_child = NULL;
    return res;
}

void make_tree(node *root,unsigned int key)
{
    node *n = make_node(key);
    node *ptr = root;
    while (ptr)
    {
        if (ptr->data > n->data)
        {
            if (ptr->left_child)
            {
                ptr = ptr->left_child;
                
            }
            else
            {
                ptr->left_child = n;
                break;
            }
        }
        else
        {
            if (ptr->right_child)
            {
                ptr = ptr->right_child;
                
            }
            else
            {
                ptr->right_child = n;
                break;
            }
        }
    }
}


int main()
{
    unsigned int key;
    scanf("%u",&key);
    node * root = make_node(key);

    while (scanf("%u", &key) == 1)
    {
        make_tree(root,key);
    }

    postorder(root);
}