from votekit import load_csv, remove_noncands
from votekit.elections import STV, random_transfer
import jsonlines
import sys
import os
import time

def run_experiment(num_trials, preference_profile, verbose=False):
    '''
    Runs fractional vs. random transfer experiment.

    Args:
        num_trials (int): number of trials to run
        election (str): path to election results 
        verbose (bool): output number of iterations 

    Returns: List of election results for all trials
    '''

    results = []
    for i in range(num_trials):
        if verbose and i % 10 == 0:
            print('Trial Number:', i)

        election = STV(preference_profile, transfer=random_transfer, seats=6, ballot_ties=False)
        election_results = election.run_election()
        results.append(election_results.to_dict(keep=['elected', 'ranking']))
     
    return results


def main():
    if len(sys.argv) != 3: 
        print('Must input number of trials and range of years')
        sys.exit(1)
    
    lb, ub = sys.argv[2].split('-')
    num_trials = int(sys.argv[1])

    for year in range(int(lb), int(ub)+1, 2):
        profile = load_csv(f'data/cambridge_school_{year}.csv')

    # need a better way of determining non-cands 
        to_remove = ['skipped', '0)']
        cambridge = remove_noncands(profile, to_remove)
        results = run_experiment(num_trials, cambridge, verbose=True)

        os.makedirs('output', exist_ok=True)
        with jsonlines.open(f'output/school_random_cambridge_{year}.jsonl', 'w') as out:
            out.write_all(results)

        time.sleep(5)
        os.system('pmset sleepnow')
        

if __name__ == '__main__':
    main()