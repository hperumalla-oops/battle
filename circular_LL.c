#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node *link;
};
typedef struct node Node;

void display(Node *head){
    Node *temp=head;
    while(temp->link !=head){
        printf("%d ",temp->data);
        temp=temp->link;
    }
    printf("%d\n ",temp->data);

}

Node* killed(Node *head, int n){
    Node *temp=head;
    int j=0;
    while(temp->link != temp){
        for(int i=0; i<n-1; i++){
            temp=temp->link;
        }
        temp->link=temp->link->link;
        temp=temp->link;
        j=j+1;
        printf("%dth kill: ",j);
        display(temp);
    }
    return temp;
}



Node* insert_end(Node *head, int x){
    Node *temp;
    Node *current=(Node*)malloc(sizeof(Node));
    if(head->link ==NULL){
        temp=head;
        current->data=x;
        current->link=head;
        temp->link=current;
        temp=temp->link;
    }
    else{
        current->data=x;
        current->link=head;
        temp->link=current;
        temp=temp->link;
    }
    return head;
}


int main(){
    Node *head=(Node*)malloc(sizeof(Node));
    int x;
    printf("..");
    scanf("%d",&x);
    head->data=x;
    head->link=NULL;

    while(1){
         printf("..");
        scanf("%d",&x);
        if(x==-1)
            break;
        head=insert_end(head, x);
    }

    display(head);
    Node *temp=killed(head,2);
    printf("survivor: ");
    display(temp);
    
}