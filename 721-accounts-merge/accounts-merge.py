class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict

        group_map = {}  # email -> group_ref
        groups = defaultdict(set)  # group_ref -> set of emails
        name_map = {}  # group_ref -> name
        group_id = 1

        for account in accounts:
            name = account[0]
            emails = account[1:]

            # Find all group_refs this account is already connected to
            connected_groups = set()
            for email in emails:
                if email in group_map:
                    connected_groups.add(group_map[email])

            if not connected_groups:
                # New group
                ref = f"ref_{group_id}"
                group_id += 1
            else:
                # Merge all connected groups into one
                ref = connected_groups.pop()
                for other_ref in connected_groups:
                    groups[ref] |= groups[other_ref]
                    for e in groups[other_ref]:
                        group_map[e] = ref
                    del groups[other_ref]
                    del name_map[other_ref]

            # Add current emails to the group
            for email in emails:
                groups[ref].add(email)
                group_map[email] = ref

            name_map[ref] = name  # Update name for this group

        # Prepare final result
        res = []
        for ref in groups:
            res.append([name_map[ref]] + sorted(groups[ref]))

        return res
