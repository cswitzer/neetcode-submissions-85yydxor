class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Each node starts as the leader of its own component
        leader = {i: i for i in range(n)}

        # Size of each component (only meaningful for leaders)
        component_size = {i: 1 for i in range(n)}

        def find_leader(node: int) -> int:
            """
            Find the leader of this node's component.
            Apply path compression so future lookups are faster.
            """
            current = node

            # Walk upward until a node leads itself
            while current != leader[current]:
                # Point directly to grandparent to flatten the tree
                leader[current] = leader[leader[current]]
                current = leader[current]

            return current

        def merge_components(a: int, b: int) -> bool:
            """
            Merge the components of a and b if they have different leaders.
            Returns True if a merge occurred, False otherwise.
            """
            leader_a = find_leader(a)
            leader_b = find_leader(b)

            # Already in the same group
            if leader_a == leader_b:
                return False

            # Attach smaller group under larger group’s leader
            if component_size[leader_a] < component_size[leader_b]:
                leader[leader_a] = leader_b
                component_size[leader_b] += component_size[leader_a]
            else:
                leader[leader_b] = leader_a
                component_size[leader_a] += component_size[leader_b]

            return True

        # Start with n separate components
        components = n

        # Each successful merge reduces component count by 1
        for node1, node2 in edges:
            if merge_components(node1, node2):
                components -= 1

        return components
