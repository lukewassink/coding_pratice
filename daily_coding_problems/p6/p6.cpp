// An XOR linked list is a more memory efficient doubly linked list. Instead of
// each node holding next and prev fields, it holds a field named both, which
// is an XOR of the next node and the previous node. Implement an XOR linked
// list; it has an add(element) which adds the element to the end, and
// a get(index) which returns the node at index.

#include <iostream>
#include <stdint.h>

using std::cout;

template <typename V>
struct Node {
  V val;
  uintptr_t both;
  Node(V v): val(v), both(0) {}
};

template <typename V>
class XORLinkedList {
  Node<V>* begin = nullptr;
  Node<V>* end = nullptr;
  int length = 0;

  public:

  void add(V val) {
    Node<V>* n = new Node<V>(val);
    length++;
    if (begin == nullptr) {
      begin = n;
      end = n;
      return;
    }

    end->both = end->both ^ reinterpret_cast<uintptr_t>(n);
    n->both = reinterpret_cast<uintptr_t>(end);
    end = n;
  }

  Node<V>* get(int i) {
    if (i >= length) return nullptr;

    Node<V>* prev = nullptr;
    Node<V>* n = begin;
    for (int j = 0; j < i; j++) {
      Node<V>* temp = n;
      n = reinterpret_cast<Node<V>*>(n->both ^ reinterpret_cast<uintptr_t>(prev));
      prev =  temp;
    }
    return n;
  }
};

int main() {
  XORLinkedList<std::string> l;
  cout << "\nEmpty: " << (l.get(3) == nullptr);
  l.add("one");
  cout << "\nOne element: " << l.get(0)->val;
  l.add("two");
  l.add("three");
  cout << "\nOne: " << l.get(0)->val;
  cout << "\nTwo: " << l.get(1)->val;
  cout << "\nThree: " << l.get(2)->val;
  cout << "\nToo big: " << (l.get(3) == nullptr);
  return 0;
}
