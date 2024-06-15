On Poems Categorisation
=======================

There exists a discernible gap in the systematic categorisation and citation methodologies applied to books in contrast to the ones applied to individual poems, as well as other self-contained literary works, such as chronicles and short stories.
Such that the prevailing standard for citation, namely BibTeX, lacks a dedicated entry for those [*]_.

One could argue the ``@inbook`` entry may fulfill the purpose.
However, according to BibTeX [#bibtex]_, ``@inbook`` is reserved for 'a section or chapter in a book'.
Naturally, individual poems do not constitute a section or chapter in the conventional way, and it seems far-fetched to try to fit them into this category.

Another argument would be to use the ``@misc`` entry, which is 'used if nothing else fits' [#bibtex]_.
It seems reasonable that websites, flyers, interviews, audio recordings, and such fit into the miscellaneous category.
Those formats and technologies have appeared long after most of the canonical materials used as sources of information existed, which are the ones BibTeX supports (books, collection, thesis).
Nonetheless, poems, being as old as the very concept of books, deserve a distinct categorisation.

Furthermore, the fact that many poems are not contained in either books or anthologies emphasizes the need for a specific entry.
Take Sappho's [#sappho]_ poetry, for example. Only isolated poems and fragments exist [#sapphobook]_.
Though no anthology existed when Sappho was alive, each poem exists on its own and the format of publication must assume the role of a secondary field, as opposed to citing a poem within a book as a mere page number.

In fact, the recurrent gathering, reorganization, and (re)publication of these works in diverse anthologies underscore their autonomy.
With the exception of anthologies compiled and published by the original authors in life, sporadically published works are typically reorganized and reissued by publishers or copyright holders into different forms and books.
(There are certainly numerous examples of this, and `here <#appendix-example-of-reissuing>`_ is one.)

Solution
--------

When I first wrote this document, I was convinced that a new entry type, ``@poem`` should be implemented as a solution.
However, upon further research, it seems that BibLaTeX solved this issue by simply expanding on the concept of the existing ``@inbook`` entry.

According to BibLaTeX documentation, the ``@inbook`` is recommended for 'a self-contained part of a book with its own title **only**'. Emphasis is given on the word 'only' by me.
The following lines of the documentation state that 'if you want to refer to a chapter or section of a book, simply use the book type and add a chapter and/or pages field'.

Conclusion
----------

Therefore, BibLaTeX solves the issue: to use ``@inbook``.

It would be good, nonetheless, if there were an alias, e.g., ``@poem`` that could mimic the ``@inbook`` almost exactly, and maybe even add more fields to it, such as ``poemdate``, since many poets write down the dates their poems were written.
All that being said, I believe there should be an entry type that aims at highlighting the independent nature of a poem; a categorization that reflects its autonomy.


.. rubric:: Footnotes

.. [*] From this point on, I will only refer to poems, specifically. However, as stated before, the same applies to short-stories, novellas, chronicles, and any other form of self-contained literary work.

.. rubric:: References

.. [#bibtex] https://www.bibtex.com/g/bibtex-format/
.. [#sappho] https://en.wikipedia.org/wiki/Sappho
.. [#sapphobook] Lardinois, André. Sappho: A New Translation of the Complete Works. Edited by Diane J. Rayor. 2nd ed. Cambridge: Cambridge University Press, 2023.
.. [#bibtexdocs] https://mirrors.ibiblio.org/CTAN/macros/latex/contrib/biblatex/doc/biblatex.pdf
.. [#contos] https://www.editora34.com.br/detalhe.asp?id=940
.. [#narrativas] https://www.editora34.com.br/detalhe.asp?id=250
