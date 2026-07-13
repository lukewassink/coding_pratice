#include <utility>

class IntHolder {
  private:

    int* value;

  public:

    explicit IntHolder(int x) {
      value = new int(x);
    }

    ~IntHolder() {
      delete value;
    }

    IntHolder(const IntHolder& other) {
      value = new int(*other.value);
    }

    IntHolder(IntHolder&& other) : value(other.value) noexcept {
      other.value = nullptr;
    }

    IntHolder& operator=(const IntHolder& other) {
      if (this != &other) {
        int* copy = new int(other.value);
        delete value;
        value = copy;
      }

      return *this;
    }

    IntHolder& operator=(IntHolder&& other) noexcept {
      if (this != &other) {
        delete value;

        value = other.value;
        other.value = nullptr;
      }

      return *this;
    }

    int get() const {
      return *value;
    }
};

int main() {
  IntHolder a(5);
  IntHolder b = a;              // copy

  IntHolder c = std::move(a);   // move

  b = c;                        // copy assignment

  c = IntHolder(42);            // move assignment
}
