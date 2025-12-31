# frozen_string_literal: true
# priority_queue.rb
#
# A binary heap-based priority queue implementation for Ruby.
#
# @author Ye Gao
# @since 2025-12-31

module CPLib
  VERSION = "0.0.1"
  # A priority queue implementation using a binary heap.
  #
  # By default, this is a min-heap (smallest priority value is dequeued first).
  # Pass a custom comparator to create a max-heap or custom ordering.
  #
  # @example Basic usage (min-heap)
  #   pq = Collections::PriorityQueue.new
  #   pq.push(5)
  #   pq.push(1)
  #   pq.pop  # => 1
  #
  # @example Max-heap using custom comparator
  #   pq = Collections::PriorityQueue.new { |a, b| a >= b }
  #   pq.push(1)
  #   pq.push(10)
  #   pq.pop  # => 10
  #
  class PriorityQueue
    include Enumerable
    # Returns the number of elements in the queue.
    # @return [Integer] the current size of the queue
    attr_reader :size
    alias length size
    # Creates a new PriorityQueue.
    #
    # @param init [Array, nil] optional array to start with.
    # @param block [Proc, nil] optional comparison block for custom ordering.
    #   Should return true/false (like >=). Defaults to min-heap behavior.
    # @yield [a, b] optional block to evaluate heap order
    # @yieldparam a [Object] first priority to compare
    # @yieldparam b [Object] second priority to compare
    # @yieldreturn [Boolean] true/false
    #
    # @example Create a max-heap
    #   pq = PriorityQueue.new { |a, b| a >= b }
    #
    def initialize(init=nil, &block)
      @heap = init || []
      @cmp = block || lambda{|x, y| x <= y}
      heapify if !@heap.empty?
    end
    # Adds an element to the priority queue.
    #
    # @param elem [Object] the element to add
    # @return [void]
    #
    # @example
    #   pq.push(5)
    #
    def push(elem)
      @heap << elem
      swim(@heap.size - 1)
    end
    alias << push
    alias enqueue push
    # Removes and returns the element with the highest priority.
    #
    # @return [Object, nil] the element with highest priority, or nil if empty
    #
    # @example
    #   pq.push(1)
    #   pq.pop  # => 1
    #   pq.pop  # => nil
    #
    def pop
      return nil if empty?
      swap(0, @heap.size - 1)
      ans = @heap.pop
      sink(0)
      ans
    end
    alias dequeue pop
    # Returns the element with the highest priority without removing it.
    #
    # @return [Object, nil] the element with highest priority, or nil if empty
    #
    # @example
    #   pq.push(1)
    #   pq.peek  # => "a"
    #   pq.peek  # => "a" (still there)
    #
    def peek
      return nil if empty?
      @heap.first
    end
    alias first peek
    alias top peek
    # Checks if the queue is empty.
    #
    # @return [Boolean] true if the queue has no elements
    #
    def empty?
      @heap.empty?
    end
    # Returns a string representation of the queue.
    #
    # @return [String] string representation
    #
    def to_s
      @heap.join(' ')
    end
    alias inspect to_s

    private
    # Turns the array into a heap.
    # @return [void]
    def heapify
      (size-1).downto(0) do |k|
        sink(k)
      end
    end
    # Restores heap property by swimming element up.
    # @param k [Integer] the index to start from
    # @return [void]
    def swim(k)
      while k > 0
        p = (k-1)/2
        break if @cmp.call(@heap[p], @heap[k])
        swap(p, k)
        k = p
      end
    end
    # Restores heap property by sinking element down.
    # @param k [Integer] the index to start from
    # @return [void]
    def sink(k)
      while 2*k+1 < @heap.length
        c = 2*k+1
        c += 1 if c+1 < @heap.length && !@cmp.call(@heap[c], @heap[c+1])
        break if @cmp.call(@heap[k], @heap[c])
        swap(k, c)
        k = c
      end
    end
    # Swaps two elements.
    # @param i [Integer] the 1st index 
    # @param j [Integer] the 2nd index 
    # @return [void]
    def swap(i, j)
      @heap[i], @heap[j] = @heap[j], @heap[i]
    end
  end
end