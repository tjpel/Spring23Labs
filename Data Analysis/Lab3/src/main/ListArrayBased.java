package main;

public class ListArrayBased implements ListInterface {
	private static final int MAX_ITEMS = 25;
	private Object items[];   // To hold everything
	private int numItems; 	// To track how many things in list
	
	// TODO: Initialize the member variables using default
	//			constructor.
	public ListArrayBased(){
		items = new Object[MAX_ITEMS];
		numItems = 0;
	}
	
	// TODO: Write a function to determine if there's anything
	//			in the list
	public boolean isEmpty() {
		if(numItems == 0) {
			return true;
		}else {
			return false;
		}
	}

	
	//TODO: Write a function that returns the size of list
	public int size(){
		return numItems;
	}
	
	//TODO: Write a function that removes all items from list

	
	//TODO: Write a function that adds an item to list.
	//			Should throw an exception if no room left in list.
	public void add(int index, Object s) throws ListIndexOutOfBoundsException
	{
		// List is full
		if(numItems== MAX_ITEMS)
		{
			throw new ListIndexOutOfBoundsException("No space left in list.");
		}else if(index >= 0 && index <= numItems){ //index is in the list
			// Shift old items
			for(int i = numItems-1; i >= index; i--) {
				items[i+1] = items[i];
			}

			// Store new item
			items[index] = s;
			
			numItems++;
		}else{
			/* Throw exception here */
			throw new ListIndexOutOfBoundsException("Invalid index!");
		}	
	}
	
	//TODO: Write a function that returns item at specified index.
	public Object get(int index) throws ListIndexOutOfBoundsException{
		if(index < 0 || index > numItems-1){
			throw new ListIndexOutOfBoundsException("Can't retrieve item. Requested index out of bounds.");
		}else{
			return items[index];
		}
	}
	
	//TODO: Write a function that removes an item at specified index.
	public void remove(int index) throws ListIndexOutOfBoundsException{
		// Check situation where index is out of range
		if(index<0 || index >= numItems){
			/* Throw an exception here */
		}else{
			/* Shift items here */

			// Need to decrement number of items in list
			numItems--;
		}
	}
	
	
	// To help us debug the code--converts all elements to single string
	public String toString()
	{
		String s = "";
		
		for(int i = 0; i < size(); i++)
		{
			s += (items[i] + " ");
		}
		
		return s;
	}

}
