# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 18:54:35 2018

@author: Muhammad Rifky Y
"""

class Stack:
    def __init__(self,elem=None):
        self.elem=elem
        self.next=None
    def __str__(self):
        if self.next==None:
            return('{0}'.format(self.elem))
        return('{0},{1}'.format(self.elem,self.next))
    def __iter__(self):
        self.now=self
        return self
    def __next__(self):
        if self.now==None:
            raise StopIteration
        else:
            ans=self.now
            self.now=self.now.next
            return ans
    def __contains__(self,elem):
        for x in self:
            if x.elem==elem:
                return True
        return False
    def __len__(self):
        ans=0
        if self.elem!=None:
            for x in self:
                ans+=1
        return ans
    def push(self,elem):
        if self.elem==None:
            self.elem=elem
            self.next=None
        else:
            tmp=self
            while tmp.next!=None:
                tmp=tmp.next
            tmp.next=Stack(elem)
    def pop(self):
        if len(self)==1:
            ans=self.elem
            self.elem=None
            return ans
        tmp=self
        while tmp.next.next!=None:
            tmp=tmp.next
        ans=tmp.next.elem
        tmp.next=None
        return ans
    def last(self):
        tmp=self
        while tmp.next!=None:
            tmp=tmp.next
        return tmp.elem

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
    def __str__(self):
        return "{0},{1}".format(self.data,self.next)
    def __contains__(self,data):
        if isinstance(self.data,(list,tuple)):
            for i in self.data:
                if i ==data:
                    return True
        else:
            if self.data==data:
                return True
            else:
                return False
    def dataislist(self):
        if isinstance(self.data,(list,tuple)):
            return True
        return False

class DLL:
    def __init__(self):
        self.head=None
        self.tail=None
        self.sortlist=[]
        return
    def __len__(self):
        count=0
        current_node=self.head
        while current_node is not None:
            if current_node.dataislist():
                for i in range(len(current_node.data)):
                    count+=1
            else:
                count+=1
            current_node=current_node.next
        return count
    def __str__(self):
        current_node=self.head
        somestring=""
        while current_node is not None:
            if current_node.next is not None:
                somestring+=str(current_node.data)+", "
            else:
                somestring+=str(current_node.data)
            current_node=current_node.next
        return somestring
    def __contains__(self,value):
        current_node=self.head
        while current_node is not None:
            if value in current_node:
                return True
            current_node=current_node.next
        return False
    def print_list(self):
        return self.sortlist
    def depth(self):
        DLLdepth=0
        current_node=self.head
        while current_node is not None:
            DLLdepth+=1
            current_node=current_node.next
        return DLLdepth
    def search(self,value):
        current_node=self.head
        node_id=1
        result=[]
        while current_node is not None:
            if value in current_node:
                result.append(node_id)
            current_node=current_node.next
            node_id+=1
        return result
    def push_back(self,value):
        if self.head is None: #for the 1st value
            self.head=value
            value.prev=None
            value.next=None
            self.tail=value
        else:
            current_node=self.head
            while True:
                if isinstance(current_node.data,(int,float)):
                    current_node.data=[current_node.data]
                if current_node.next is not None:
                    if len(current_node.next.data)<2*len(current_node.data):
                        current_node.next.data.append(value.data)
                        return
                    else:
                        current_node=current_node.next
                else:
                    value.data=[value.data]
                    self.tail.next=value
                    value.prev=self.tail
                    self.tail=value
                    return
    def push_front(self,value):
        value.data=[value.data]
        if self.tail is None:
            self.head=value
            value.prev=None
            value.next=None
            self.tail=value
        else:
            if isinstance(self.head.data,(int,float)):
                self.head.data=[self.head.data]
            self.head.prev=value
            value.next=self.head
            self.head=value
        return
    def remove(self,value):
        current_node=self.tail
        while current_node is not None:
            previous_node=current_node.prev
            next_node=current_node.next
            if value.data in current_node.data:
                current_node.data.remove(value.data)
                if not len(current_node.data):
                    if previous_node is not None:
                        previous_node.next=next_node
                        if next_node is not None:
                            next_node.prev=previous_node
                    else:
                        self.head=next_node
                        if next_node is not None:
                            next_node.prev=None
                return
            current_node=current_node.prev
    def heapify(self):
        while True:
            current_node=self.tail.prev
            issorted=True
            while current_node is not None:
                for i in range(len(current_node.data)):
                    haschildren=False
                    haschild=False
                    try:
                        tes=max(current_node.next.data[2*(i+1)-1],current_node.next.data[2*(i+1)-2])
                        haschildren=True
                    except:
                        pass
                    if haschildren:
                        if current_node.data[i]<tes:
                            if current_node.next.data[2*(i+1)-2]==tes:
                                current_node.next.data[2*(i+1)-2],current_node.data[i]=current_node.data[i],current_node.next.data[2*(i+1)-2]
                            else:
                                current_node.next.data[2*(i+1)-1],current_node.data[i]=current_node.data[i],current_node.next.data[2*(i+1)-1]
                        continue
                    try:
                        current_node.next.data[2*(i+1)-2]
                        haschild=True
                    except:
                        pass
                    if haschild:
                        if current_node.data[i]<current_node.next.data[2*(i+1)-2]:
                            current_node.next.data[2*(i+1)-2],current_node.data[i]=current_node.data[i],current_node.next.data[2*(i+1)-2]
                        continue
                current_node=current_node.prev
            current_node=self.head
            while current_node is not None:
                for i in range(len(current_node.data)):
                    haschildren=False
                    haschild=False
                    try:
                        tes1=current_node.next.data[2*(i+1)-2]
                        haschild=True
                        tes=max(current_node.next.data[2*(i+1)-1],current_node.next.data[2*(i+1)-2])
                        haschildren=True
                    except:
                        pass
                    if haschildren:
                        if current_node.data[i]<tes:
                            issorted=False
                            break
                    if haschild:
                        if current_node.data[i]<tes1:
                            issorted=False
                            break
                current_node=current_node.next
            if issorted:
                break
    def sort(self):
        while self.head.data!=[]:
            self.heapify()
            self.sortlist.append(self.head.data.pop())
            try:
                if self.tail.data==[]:
                    self.tail=self.tail.prev
                    self.tail.next=None
                    self.head.data.append(self.tail.data.pop())
                else:
                    self.head.data.append(self.tail.data.pop())
            except IndexError:
                pass
            
class BinaryTree:
    def __init__(self,key=None):
        self.prev=None
        self.root = key
        self.left = None
        self.right = None
        self.nodecount=0
        self.level=0
    def __str__(self):
        if self.right is None:
            if self.left is None:
                return "({0})".format(self.root)
            return "({0},{1})".format(self.root,self.left)
        return "({0},{1},{2})".format(self.root,self.left,self.right)
    def append_rootL(self,data):
        tmp=self
        self.prev.data=data
        self.prev.left=tmp
    def set_root(self, key):
        self.root = key
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.key, end=' ')
        if self.right is not None:
            self.right.inorder()
    def search(self, key):
        if self.root == key:
            return self
        if self.left is not None:
            temp =  self.left.search(key)
            if temp is not None:
                return temp
        if self.right is not None:
            temp =  self.right.search(key)
            return temp
        return None   
    def insert(self,key):
        if isinstance(key,DLL):
            current_node=self
            current_value=key.head
            self.nodecount=1
            for i in range(key.depth()-1):
                for j in range(len(current_value.data)):
                    if current_node is None:
                        a=BinaryTree(current_value.data[j])
                        current_node=a
                        self.nodecount+=1
                    elif current_node is not None and current_node.root is None:
                        current_node.root=current_value.data[j]
                    else:
                        current_node=self.search(current_value.data[j])
                    try:
                        a=BinaryTree(current_value.next.data[2*(j+1)-2])
                        current_node.left,a.prev=a,current_node.root
                        self.nodecount+=1
                        a=BinaryTree(current_value.next.data[2*(j+1)-1])
                        current_node.right,a.prev=a,current_node.root
                        self.nodecount+=1
                    except:
                        pass
                current_value=current_value.next
            return self