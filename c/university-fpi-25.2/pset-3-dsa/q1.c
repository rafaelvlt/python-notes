#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
  int data;
  struct Node* left;
  struct Node* right;
} Node;

Node* createNode(int v);
Node* insert(Node* root, int v);
Node* search(Node* root, int v);
void print_preorder(Node* root);
void print_order(Node* root);
void print_postorder(Node* root);
void freeTree(Node* root);

int main(){
  int n = 0;
  scanf("%d", &n);
  
  int valor = 0;
  Node* root = NULL;
  for (int i = 0; i < n; i++){
    scanf("%d", &valor);
    root = insert(root, valor);
  }
  
  printf("Pre order :");
  print_preorder(root);
  printf("\n");
  printf("In order  :");
  print_order(root);
  printf("\n");
  printf("Post order:");
  print_postorder(root);
  printf("\n");
  
  freeTree(root);

  return 0;
}



Node* createNode(int v){
  Node* new = (Node*)malloc(sizeof(Node));
  if (new == NULL){
    printf("Failed to allocate for node. Exiting");
    exit(1);
  }
  new->data = v;
  new->left = NULL;
  new->right = NULL;

  return new;
}

Node* insert(Node* root, int v){
  if (root == NULL){
    Node* new = createNode(v);
    return new;
  }

  if (v < root->data){
    root->left = insert(root->left, v);
  }
  else {
    root->right = insert(root->right, v);
  }

  return root;
}

Node* search(Node* root, int v){
  if (root == NULL){
    return NULL;
  }
  else if (root->data == v){
    return root;
  }

  if (v < root->data){
    return search(root->left, v);
  }

  return search(root->right, v);
}

void print_preorder(Node* root){
  if (root != NULL){
    printf(" %d", root->data);
    print_preorder(root->left);
    print_preorder(root->right);
  }
}

void print_order(Node* root){
  if (root != NULL){
    print_order(root->left);
    printf(" %d", root->data);
    print_order(root->right);
  }
}

void print_postorder(Node* root){
  if (root != NULL){
    print_postorder(root->left);
    print_postorder(root->right);
    printf(" %d", root->data);
  }
}
void freeTree(Node* root){
  if (root == NULL) return;
  freeTree(root->left);
  freeTree(root->right);
  free(root);
}

