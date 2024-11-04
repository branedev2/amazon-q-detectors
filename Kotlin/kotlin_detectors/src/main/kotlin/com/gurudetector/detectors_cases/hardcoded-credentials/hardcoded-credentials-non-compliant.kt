/*
*  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
*  SPDX-License-Identifier: Apache-2.0
*/

// {fact rule=kotlin-hardcoded-credentials@v1.0 defects=1}
import net.schmizz.sshj.SSHClient

// Noncompliant: Password is hardcoded.
fun hardcoded_credentials_noncompliant() {
    val username = "admin"
    val password = "password123"
    val ssh = SSHClient()
    ssh.authPassword(username, password)
}
// {/fact}