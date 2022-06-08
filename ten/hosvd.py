from typing import Sequence

import numpy as np
from numpy.typing import ArrayLike


def hosvd(a: ArrayLike) -> tuple[ArrayLike, Sequence[ArrayLike]]:
    """Higher-order singular value decomposition (HOSVD)

    parameters
    ----------
    - a. ArrayLike

    returns
    -------
    - S. ArrayLike
    - U. Sequence[ArrayLike]
    """

    Us = []
    Ak = a

    for k in range(a.ndim):
        # fold Ak
        Ak = np.moveaxis(Ak, k, 0)
        shape = list(Ak.shape)
        Ak = np.reshape(Ak, (Ak.shape[0], -1))

        # compute SVD
        u, s, vh = np.linalg.svd(Ak, full_matrices=False, compute_uv=True, hermitian=False)
        shape[0] = len(s)

        # unfold Ak for next iteration
        Ak = np.atleast_2d(s).T * vh
        Ak = np.reshape(Ak, shape)

        Us.append(u)

    Ak = Ak.transpose()
    return (Ak, Us)
