# flake8: noqa

from nop import nop

(
    # ,+[
    ~nop() + 1 >> (
        # -[
        nop() - 1 >> (
            nop()

            # >>++++
            > nop()
            > nop() + 4

            # [>++++++++<-]
            >> (
                nop()

                > nop() + 8
                < nop() - 1
            ) << nop()

            # <+<-
            < nop() + 1
            < nop() - 1

            # [
            >> (
                nop()

                # >+>+>-
                > nop() + 1
                > nop() + 1
                > nop() - 1

                # [>>>]
                >> (
                    nop() > nop() > nop() > nop()
                ) << nop()

                # <[
                < nop() >> (
                    # [>+<-]
                    nop() >> (
                        nop()

                        > nop() + 1
                        < nop() - 1
                    # ]
                    ) << nop()

                    # >>+>
                    > nop()
                    > nop() + 1
                    > nop()

                # ]
                ) << nop()

                # <<<<<-
                < nop()
                < nop()
                < nop()
                < nop()
                < nop() - 1

            # ]
            ) << nop()

        # ]
        ) << nop()

        # >>>
        > nop()
        > nop()
        > nop()

        # [-]
        >> ( nop() - 1 ) << nop()

        # +>--
        + 1 > nop() - 2

        # [-
        >> (
            nop() - 1

            # [<->+++[-]]
            >> (
                nop() < nop() - 1 > nop() + 3 >> (
                    nop() - 1
                ) << nop()
            ) << nop()

        # ]
        ) << nop()

        # <[
        < nop() >> (
            nop()

            # ++++++++++++
            + 12

            # <[
            < nop() >> (
                nop()

                # >-[>+>>]
                > nop() - 1 >> ( nop() > nop() + 1 > nop() > nop() ) << nop()

                # >[
                > nop() >> (
                    # +[<+>-]
                    nop() + 1 >> (
                        nop() < nop() + 1 > nop() - 1
                    ) << nop()

                    # >+>>
                    > nop() + 1
                    > nop()
                    > nop()

                # ]
                ) << nop()
            
                # <<<<<-
                < nop()
                < nop()
                < nop()
                < nop()
                < nop() - 1

            # ]
            ) << nop()

            # >>
            > nop()
            > nop()

            # [<+>-]
            >> ( nop() < nop() + 1 > nop() - 1 ) << nop()

            # >[
            > nop() >> (
                # -[-<<[-]>>]
                nop() - 1 >> (
                    nop() - 1

                    < nop()
                    < nop()

                    >> ( nop() - 1 ) << nop() > nop() > nop()
                ) << nop()

                # <<
                < nop()
                < nop()

                # [<<->>-]
                >> (
                    nop() < nop() < nop() - 1 > nop() > nop() > nop() - 1
                ) << nop()

                # >>
                > nop()
                > nop()

            # ]
            ) << nop()

            # <<
            < nop()
            < nop()

            # [<<+>>-]
            >> (
                nop() < nop() < nop() + 1 > nop() > nop() - 1
            ) << nop()

        # ]
        ) << nop()

        # <[-]
        < nop() >> ( nop() - 1 ) << nop()

        # <.[-]
        < nop() ^ nop() >> ( nop() - 1 ) << nop()

        # <-,+
        < nop() - 1

        > nop() < ~nop() + 1

    # ]
    ) << nop()


).run(stdout=True)
