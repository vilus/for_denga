
class Paren(object):
    def __init__(self, idx, val):
        self.idx = idx
        self.val = val
        self._close_paren = None

    @property
    def close_paren(self):
        return self._close_paren

    @close_paren.setter
    def close_paren(self, value):
        if value == self:
            raise ValueError("Can't assignee itself as close paren")
        self._close_paren = value

    def is_left(self):
        return self.val == '('


def get_last_right_unclosed_paren(all_parens):
    all_rights = []
    all_lefts = []
    for p in all_parens:
        if p.is_left():
            all_lefts.append(p)
        else:
            all_rights.append(p)
    last_right_unclosed = None
    for rp in reversed(all_rights):
        if [p for p in all_lefts if p.close_paren == rp]:
            # may be optimized
            continue
        else:
            last_right_unclosed = rp
            break
    return last_right_unclosed


def clean_unclosed_parens(src):
    all_parens = [Paren(idx, val) for idx, val in enumerate(src) if val in ('(', ')')]

    if not all_parens:
        return src

    unclosed_parens = []
    for paren in all_parens:
        if paren.is_left():
            unclosed_parens.append(paren)
        elif unclosed_parens:
            unclosed_parens.pop().close_paren = paren

    cl = []

    def _get_cleaned(paren_idx, offset):
        if paren_idx == len(all_parens) - 1:
            # need to prepare tail
            last_paren = all_parens[-1]
            is_closed = any(p for p in all_parens if p.close_paren == last_paren)  # TODO: refact
            if is_closed:
                if offset <= len(src):
                    cl.extend(src[last_paren.idx+1:])
            else:
                if offset <= len(src):
                    cl.extend(src[offset:last_paren.idx])
            return
        # ---------------------------------------
        paren = all_parens[paren_idx]

        if not paren.is_left():
            # skip right closed paren
            return _get_cleaned(paren_idx+1, paren.idx+1)
        # ---------------------------------------
        if not paren.close_paren:
            cl.extend(src[offset:paren.idx])
            next_block = all_parens[paren_idx + 1]
            is_next_block_closed = next_block.is_left() and next_block.close_paren and paren.idx + 1 == next_block.idx
            if is_next_block_closed:
                return _get_cleaned(paren_idx+1, paren.idx)
        else:
            cl.extend(src[offset:paren.close_paren.idx+1])
            return _get_cleaned(paren_idx+1, paren.close_paren.idx+1)
        # ---------------------------------------

    last_right_unclosed_paren = get_last_right_unclosed_paren(all_parens)
    if last_right_unclosed_paren:
        # strict right ')' unclosed parens
        _get_cleaned(all_parens.index(last_right_unclosed_paren), last_right_unclosed_paren.idx)
    else:
        _get_cleaned(0, 0)
    return ''.join(cl)


def clean_unclosed_parens_re(_):
    # r'\([^\)]*?$' -> but it's not enough
    # seems like need recursive feature from `regex` pkg
    raise NotImplemented()

