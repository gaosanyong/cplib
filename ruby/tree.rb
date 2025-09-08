
module CPLib
  ##
  # A Priority Queue is a data structure similar to a regular queue, but each
  # element has a "priority." The element with the highest priority is served
  # before elements with lower priority. This implementation uses a min-heap by
  # default to store the elements, ensuring that the element with the smallest
  # value (highest priority) is always at the root of the heap.
  class PriorityQueue
    attr_reader :data

    def initialize(data = [], options = {})
      @data = data
      @is_ordered = options[:compare] || ->(p, c) {p <= c}
    end

    def heapify
      (0...size).each do |i|
        while i > 0
          j = (i-1) / 2
          break if @is_ordered.call(@data[j], @data[i])
          @data[i], @data[j] = @data[j], @data[i]
          i = j
        end
      end
    end

    def push(value)
      @data << value
      swim(size - 1)
    end

    def pop
      ans = top
      @data[0], @data[size-1] = @data[size-1], @data[0]
      @data.pop
      sink(0)
    end

    def size
      @data.size
    end

    def top
      @data[0]
    end

    private

    def sink(k)
      while 2*k+1 < size
        c = 2*k+1
        c += 1 if c+1 < size && !@is_ordered.call(@data[c], @data[c+1])
        break if @is_ordered.call(@data[k], @data[c])
        @data[k], @data[c] = @data[c], @data[k]
        k = c
      end
    end

    def swim(k)
      while k > 0
        p = (k-1) / 2
        break if @is_ordered.call(@data[p], @data[k])
        @data[p], @data[k] = @data[k], @data[p]
        k = p
      end
    end
  end
end
