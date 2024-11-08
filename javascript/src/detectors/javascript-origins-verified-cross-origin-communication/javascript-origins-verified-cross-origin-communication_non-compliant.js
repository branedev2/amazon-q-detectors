// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

// {fact rule=javascript-origins-verified-cross-origin-communication@v1.0 defects=1}
function originsVerifiedCrossOriginCommunicationsNoncompliant() {
    var iframe = document.getElementsByClassName(".testiframe")
    // Noncompliant: The wildcard keyword `*` is used.
    iframe.contentWindow.postMessage("secret_value", "*")
}
// {/fact}
