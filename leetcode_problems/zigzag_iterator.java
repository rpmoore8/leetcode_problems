/*
///////////////
Zigzag Iterator
///////////////

Given two 1d vectors, implement an iterator to return their elements alternately.

Example:
Input:
v1 = [1,2]
v2 = [3,4,5,6] 

Output: [1,3,2,4,5,6]

Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,3,2,4,5,6].
Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question:
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example:

Input:
[1,2,3]
[4,5,6,7]
[8,9]

Output: [1,4,8,2,5,9,3,6,7].

Difficulty: MEDIUM
*/

public class ZigzagIterator {

    public List<Integer> l1;
    public List<Integer> l2;
    public boolean flip = true;
    public ListIterator<Integer> litr1;
    public ListIterator<Integer> litr2;

    public ZigzagIterator(List<Integer> v1, List<Integer> v2) {
        l1 = v1;
        l2 = v2;
        litr1 = v1.listIterator();
        litr2 = v2.listIterator();
    }

    public int next() {
        if (flip) {
            flip = false;
            return litr1.next();
        } else {
            flip = true;
            return litr2.next();
        }
    }

    public boolean hasNext() {
        if (flip) {
            if (litr1.hasNext()) {
                return true;
            } else if (litr2.hasNext()) {
                flip = false;
                return true;
            } else {
                return false;
            }
        } else {
            if (litr2.hasNext()) {
                return true;
            } else if (litr1.hasNext()) {
                flip = true;
                return true;
            } else {
                return false;
            }
        }
    }
}

/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i = new ZigzagIterator(v1, v2); while (i.hasNext()) v[f()] =
 * i.next();
 */