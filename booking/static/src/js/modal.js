$(document).ready(() => {
    // Store modals container in a dictionary
    const modals = {
        loginModal: $('.login-modal'),
        signupModal: $('.signup-modal'),
        bookingModal: $('.booking-modal'),
        voterModal: $('.voter-modal'),
        documentModal: $('.document-modal')
    }

    // Modal handlers
    HandleLogin(modals);
    HandleSignin(modals);
    HandleBooking(modals);
    HandleVoter(modals);
    HandleDocument(modals);
})

const HandleVoter = modals => {
    // Voter modal
    $('#voter-btn').click(() => {
        HideAllExcept(modals, modals.voterModal);

        modals.voterModal.removeClass('hide');
    })

    // Hide modal
    $(document).click(e => {
        if (e.target === modals.voterModal[0]) {
            // Hide modal
            modals.voterModal.addClass('hide');
        }
    })
}

const HideAllExcept = (modals, exceptModal) => {
    // Hide all modals stored in the dictionary except the exception
    for (var prop in modals) {
        if (modals[prop] === exceptModal) continue;
        modals[prop].addClass('hide');
    }
}

const HandleLogin = modals => {
    // Login modal
    $('.login-btn').click(() => {
        // Hide all other modals
        HideAllExcept(modals, modals.loginModal);

        modals.loginModal.removeClass('hide');
    })

    // Hide modal
    $(document).click(e => {
        if (e.target === modals.loginModal[0]) {
            // Hide modal
            modals.loginModal.addClass('hide');
        }
    })
}

const HandleSignin = modals => {
    // Signin modal
    $('#signup-btn').click(() => {
        // Hide all other modals
        HideAllExcept(modals, modals.signupModal);

        modals.signupModal.removeClass('hide');
    })

    // Hide modal
    $(document).click(e => {
        if (e.target === modals.signupModal[0]) {
            // Hide modal
            modals.signupModal.addClass('hide');
        }
    })
}

const HandleBooking = modals => {
    // Booking modal
    $('#booking-btn').click(() => {
        HideAllExcept(modals, modals.bookingModal);

        modals.bookingModal.removeClass('hide');
    })

    // Hide modal
    $(document).click(e => {
        if (e.target === modals.bookingModal[0]) {
            // Hide modal
            modals.bookingModal.addClass('hide');
        }
    })
}
const HandleDocument = modals => {
    // Booking modal
    $('#document-btn').click(() => {
        HideAllExcept(modals, modals.documentModal);

        console.log(modals.documentModal);

        modals.documentModal.removeClass('hide');
    })

    // Hide modal
    $(document).click(e => {
        if (e.target === modals.documentModal[0]) {
            // Hide modal
            modals.documentModal.addClass('hide');
        }
    })
}