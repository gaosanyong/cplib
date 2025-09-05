module CPLib

  ##
  # This class provides key functionalities related to binary tree such as
  # preorder, inorder and postorder traversals.
  class BiTree

    ##
    # Traverse a binary tree rooted at +node+ in preorder.
    def self.preorder(node)
      ans = []
      stack = [node]
      while stack.any?
        node = stack.pop
        ans << node.val
        stack << node.right if node.right
        stack << node.left if node.left
      end
      ans
    end

    ##
    # Traverse a binary tree rooted at +node+ in inorder.
    def self.inorder(node)
      ans = []
      stack = []
      while node || stack.any?
        if node
          stack << node
          node = node.left
        else
          node = stack.pop
          ans << node.val
          node = node.right
        end
      end
      ans
    end

    ##
    # Traverse a binary tree rooted at +node+ in postorder.
    def self.postorder(node)
      ans = []
      prev, stack = nil, []
      while node || stack.any?
        if node
          stack << node
          node = node.left
        else
          node = stack[-1]
          if node.right && node.right != prev
            node = node.right
          else
            ans << node.val
            stack.pop
            prev, node = node, nil
          end
        end
      end
      ans
  end

end
