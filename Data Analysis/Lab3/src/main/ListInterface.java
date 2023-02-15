package main;

public interface ListInterface {
	public boolean isEmpty();
	public int size();
	public void add(int index, Object item)
		throws ListIndexOutOfBoundsException, ListException;
	public Object get(int index)
		throws ListIndexOutOfBoundsException;
	public void removeAll();
	public void remove(int index);
}
