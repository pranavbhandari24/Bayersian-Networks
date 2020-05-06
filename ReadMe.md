# Description
For the Bayesian network Fig, this program computes and prints out the probability of any combination of events given any other combination of events. This program is implemented in python.

# Compile and Run

The program can be run using the following command,
        python compute_probability.py < events > given < events >
    
# Note
In general, bnet takes 1 to 6(no more, no fewer) command line arguments, as follows:
* First, there are one to five arguments, each argument specifying a variable among Burglary, Earthquake, Alarm, JohnCalls, and MaryCalls and a value equal to true or false. Each of these arguments is a string with two letters. The first letter is B (for Burglary), E (for Earthquake), A (for Alarm), J (for JohnCalls) or M (for MaryCalls). The second letter is t (for true) or f (for false). These arguments specify a combination C1 of events whose probability we want to compute. For example, in the first example above, C1 = (Burglary=true and Alarm=false), and in the second example above C1 = (Alarm=false and Earthquake=true).

* Then, optionally, the word "given" follows, followed by one to four arguments. Each of these one to four arguments is again a string with two letters, where, as before the first letter is B (for Burglary), E (for Earthquake), A (for Alarm), J (for JohnCalls) or M (for MaryCalls). The second letter is t (for true) or f (for false). These last arguments specify a combination of events C2 such that we need to compute the probability of C1 given C2. For example, in the first example above C2 = (MaryCalls=false), and in the second example there is no C2, so we simply compute the probability of C1, i.e., P(Alarm=false and Earthquake=true).

# Examples

1. To print out the probability P(Burglary=true and Alarm=false | MaryCalls=false).

        python compute_probability.py Bt Af given Mf
2. To print out the probability P(Alarm=false and Earthquake=true).

        python compute_probability.py Af Et
3. To print out the probability P(JohnCalls=true and Alarm=false | Burglary=true and Earthquake=false).

        python compute_probability.py Jt Af given Bt Ef
4. To print out the probability P(Burglary=true and Alarm=false and MaryCalls=false and JohnCalls=true and Earthquake=true).

        python compute_probability.py Bt Af Mf Jt Et