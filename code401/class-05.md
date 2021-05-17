# Linked Lists

![](https://files.realpython.com/media/Python-Linked-Lists-Guide_Watermarked.421631d9a615.jpg)
## What is a Linked List? 

A Linked List is a sequence of Nodes that are connected/linked to each other. The most defining feature of a Linked List is that each Node references the next Node in the link.

### What does it look like

*This is what a Singly Linked List looks like*

![image](https://files.realpython.com/media/Group_14.27f7c4c6ec02.png)

**Let’s talk out what exactly is happening:**

1. We are first creating Current at the Head to guarantee we are starting from the beginning. (Remember that Head is always the first node in a Linked List)

2. We create a while loop. This loop will only run if the node that Current is pointing to is not null. This also means we can guarantee that we are still looking at a Node while the loop is running.

3. Once we are in the while loop, we are checking if the value of the current node is equal to the value we are looking for. Given the logic, if that condition is true, then we have found the value we were looking for, so we return true.

4. If the Current node does not contain the value we are looking for, we then must move Current to the next node that is being referenced. Again, because the condition of this while loop is to only run if we are still at a node, we can safely traverse to the next node without fear of getting a NullReferenceException.

5. At this point, the while loop is re-evaluated. Step 3 & 4 will continue until Current reaches the end of the LinkedList. We will know we are at the last node in the linked list because the current node will be null. Once this condition becomes true, the while loop breaks, and we now know that we are at the end.

6. Once we hit the end, we know that we did not find the value and return true at any point, so the value is not in the LinkedList. We return false.