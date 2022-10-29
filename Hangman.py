#include<iostream>
using namespace std;
 struct node{
 	int data;
 	node *ptr;

 }*head=NULL;
   void insertion(){
   	int pos;
   	cout<<"enter position of insertion enter 0 for end insertion in end "<<endl;
   	cin>>pos;
   	node*temp =new node;
   	cout<<"enter the data";
    cin>>temp->data;
   	if(pos==1){
   		if(head== NULL){
   			head=temp;
   			temp->ptr=NULL;
		   }
		   else{
		   																																																																																	
		   	temp->ptr=head;
		   	head=temp;
		   }
		   
	   }
	   else if(pos==0){
	   	if(head== NULL){
   			head=temp;
   			temp->ptr=NULL;
		   }
		   else{
	   	 node *pointer;
   	pointer = head;
   
   	while(pointer->ptr!= NULL){
   	//	cout<<pointer->data<<endl;
   		pointer =pointer->ptr;
	   }
	   pointer->ptr=temp;
	   temp->ptr=NULL;
}
   
   }
   else{
   	cout<<"enter the position of insertion in middle"<<endl;
   cin>>pos;
   	if(head== NULL){
   			head=temp;
   			temp->ptr=NULL;
		   }
		     else{
			 node *pointer;
   	pointer = head;
   	while(pointer!=pos){
   	//	cout<<pointer->data<<endl;
   		pointer =pointer->ptr;
   		
	   }
	   temp->ptr=pointer->ptr;
	   temp=pointer;
	   
}

}
}


   void traverse(){
   	   node *pointer;
   	pointer = head;
   	while(pointer!= NULL){
   		cout<<pointer->data<<endl;
   		pointer =pointer->ptr;
   		
	   }
   	
   }
int main()
{
	insertion();
	
	traverse();
	
}
